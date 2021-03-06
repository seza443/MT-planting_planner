from datetime import date

from django.test import TestCase

from planner.import_vegetables_helpers import import_vegetables_to_garden
from planner.models import Garden, Vegetable, CulturalOperation

OP1_NAME = "DateOperation"
V1_NAME = "LibraryVeggie"


class ImportVegetableTests(TestCase):

    def setUp(self):
        from vegetables_library.models import Species as library_species
        self.species = library_species.objects.create(french_name="Celebrity")
        self.garden = Garden.objects.create(name="MyGarden", postal_code=1000)

    def test_import_simple_veggie(self):
        from vegetables_library.models import Variety as library_vegetable
        self.library_veggie = library_vegetable.objects.create(french_name=V1_NAME, species=self.species)
        self.assertEqual(len(self.garden.vegetable_set.all()), 0)  # Currently no vegetables in this garden
        vegetable = [self.library_veggie.id]
        import_vegetables_to_garden(self.garden.id, vegetable)
        self.assertEqual(len(self.garden.vegetable_set.all()), 1)
        self.assertEqual(Vegetable.objects.get(variety=V1_NAME).extern_id,
                         self.library_veggie.id)  # Check if the id of the original vegetable has been copied properly

    def test_import_vegetable_with_operations(self):
        from vegetables_library.models import Variety as library_vegetable

        self.second_veggie = library_vegetable.objects.create(french_name="SecondVeggie", species=self.species)
        from vegetables_library.models import COWithOffset as library_co_with_offset
        from vegetables_library.models import COWithDate as library_co_with_date
        op1 = library_co_with_date.objects.create(name=OP1_NAME, vegetable=self.second_veggie,
                                                  absoluteDate=date(2018, 10, 3))
        op2 = library_co_with_offset.objects.create(name="OffsetOp", vegetable=self.second_veggie,
                                                    previous_operation=op1, offset_in_days=3)
        library_co_with_offset.objects.create(name="SecondOffsetOp", vegetable=self.second_veggie,
                                              previous_operation=op2, offset_in_days=3)
        vegetable = [self.second_veggie.id]
        import_vegetables_to_garden(self.garden.id, vegetable)
        imported_veggie = Vegetable.objects.get(variety=self.second_veggie.french_name)
        self.assertEqual(imported_veggie.extern_id, self.second_veggie.id)
        self.assertEqual(len(CulturalOperation.objects.select_subclasses().filter(vegetable=imported_veggie)), 3)
