from django.test import TestCase, RequestFactory
from django.http import HttpResponse
from types import SimpleNamespace
from unittest.mock import MagicMock, patch
from contextlib import ExitStack


class MatchViewSmokeTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_match_executes_without_error(self):
        # Prepare a fake authenticated user
        fake_user = SimpleNamespace(is_authenticated=True, id=1)

        # Helper: simple dummy object with dynamic attributes
        class Dummy:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)

        # Fake queryset for VQuestion1
        class FakeQS:
            def __init__(self, count_value=10):
                self._count = count_value

            def exclude(self, **kwargs):
                return self

            def count(self):
                return self._count

            def values(self):
                # Provide list of dicts with ids
                return [{"id": i} for i in range(1, self._count + 1)]

        # Create request
        request = self.factory.get("/match/")
        request.user = fake_user

        # Names used for capital types; ensure we have at least 5
        capital_names = [
            "Accelerator",
            "Bonds",
            "Bootstrapped",
            "Commercial Banking",
            "Cryptocurrency",
        ]

        # Minimal dummy responses for pdf content calls
        dummy_http = Dummy(content=b"<div></div>")

        # Patches (use ExitStack to avoid deep nesting limits)
        with ExitStack() as stack:
            stack.enter_context(patch("Matching_Algorithm.views.time.sleep", return_value=None))
            stack.enter_context(patch("Matching_Algorithm.views.render_to_string", return_value="<html></html>"))
            stack.enter_context(patch("Matching_Algorithm.views.render", return_value=HttpResponse("ok")))
            stack.enter_context(patch("Matching_Algorithm.views.create_capital_type_for_user", return_value=None))

            m_payload = stack.enter_context(patch("Matching_Algorithm.views.pay_load_string"))
            m_capitalTypes = stack.enter_context(patch("Matching_Algorithm.views.capitalTypes"))
            m_capitalType = stack.enter_context(patch("Matching_Algorithm.views.CapitalType"))
            m_vq1 = stack.enter_context(patch("Matching_Algorithm.views.VQuestion1"))
            m_matches = stack.enter_context(patch("Matching_Algorithm.views.Matches_Purchased"))
            m_purchases = stack.enter_context(patch("Matching_Algorithm.views.Purchases"))
            m_letter = stack.enter_context(patch("Matching_Algorithm.views.Letter_Response"))
            m_matchdata = stack.enter_context(patch("Matching_Algorithm.views.Match_Data"))
            m_userdetail = stack.enter_context(patch("Matching_Algorithm.views.UserDetail"))
            m_userdetail2 = stack.enter_context(patch("Matching_Algorithm.views.UserDetail2"))
            m_eq = stack.enter_context(patch("Matching_Algorithm.views.EQuestions"))
            m_eq1 = stack.enter_context(patch("Matching_Algorithm.views.EQuestions1"))
            m_eq2 = stack.enter_context(patch("Matching_Algorithm.views.EQuestions2"))
            m_eq3 = stack.enter_context(patch("Matching_Algorithm.views.EQuestions3"))
            m_eq4 = stack.enter_context(patch("Matching_Algorithm.views.EQuestions4"))
            m_eq5 = stack.enter_context(patch("Matching_Algorithm.views.EQuestions5"))
            m_eq6 = stack.enter_context(patch("Matching_Algorithm.views.EQuestions6"))
            m_eq7 = stack.enter_context(patch("Matching_Algorithm.views.EQuestions7"))
            m_eq8 = stack.enter_context(patch("Matching_Algorithm.views.EQuestions8"))
            m_docs = stack.enter_context(patch("Matching_Algorithm.views.DocumentsPrepared"))

            stack.enter_context(patch("Matching_Algorithm.views.accelerator.accelerator", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.accelerator.acceleratorfaq", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.accelerator.acceleratortwelve", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.bonds.bonds", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.bonds.bondsfaq", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.bonds.bondstwelve", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.bootstratpped.bootstrapped", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.bootstratpped.bootstrappedfaq", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.bootstratpped.bootstrappedtwelve", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.commercialbanking.commercialbanking", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.commercialbanking.commercialbankingfaq", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.commercialbanking.commercialbankingtwelve", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.cryptocurrency.cryptocurrency", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.cryptocurrency.cryptocurrencyfaq", return_value=dummy_http))
            stack.enter_context(patch("Matching_Algorithm.views.cryptocurrency.cryptocurrencytwelve", return_value=dummy_http))
            # Configure payload model
            m_payload.objects.get.side_effect = Exception("no payload yet")
            m_payload.objects.create.return_value = Dummy()

            # Capital names list for matching
            m_capitalTypes.objects.values_list.return_value = capital_names

            # Each CapitalType.objects.get returns dummy with scalar weights and counter
            m_capitalType.objects.get.return_value = Dummy(matrix_weights=1, counter=1)

            # VQuestion1 filter/exclude/count/values behavior
            m_vq1.objects.filter.return_value = FakeQS(count_value=10)

            # Matches_Purchased
            m_matches.DoesNotExist = Exception
            m_matches.objects.get.side_effect = m_matches.DoesNotExist
            matches_instance = Dummy(match_id_cm=[], save=lambda: None)
            m_matches.return_value = matches_instance

            # Purchases
            m_purchases.DoesNotExist = Exception
            m_purchases.objects.get.side_effect = m_purchases.DoesNotExist
            purchases_instance = Dummy(
                cm1purchase=2,
                cm2purchase=0,
                cm3purchase=0,
                cm4purchase=0,
                cm5purchase=0,
                cm6purchase=0,
                ipurchase=0,
                save=lambda: None,
            )
            m_purchases.return_value = purchases_instance

            # Letter_Response
            m_letter.DoesNotExist = Exception
            # First .objects.get is used for status check; raise to force recompute
            m_letter.objects.get.side_effect = m_letter.DoesNotExist
            # Instantiation returns dummy with save
            m_letter.return_value = Dummy(save=lambda: None)

            # Match_Data
            m_matchdata.DoesNotExist = Exception
            m_matchdata.objects.get.side_effect = m_matchdata.DoesNotExist
            m_matchdata.return_value = Dummy(save=lambda: None)

            # UserDetail lookups
            m_userdetail.objects.get.return_value = Dummy(
                First_Name="John",
                Last_Name="Doe",
                Business_Adress="123 St",
                Business_Phone="123456",
                Mobile_Phone="987654",
                User_Email="john@example.com",
                Company_Website="https://example.com",
                Affiliation="None",
                Special_Programs="",
            )
            m_userdetail2.objects.get.return_value = Dummy(
                Primary_Purpose="Testing", Account_Type="A", Billing_Option="B"
            )

            # EQuestions aggregate (pricing and timing)
            m_eq.objects.get.return_value = Dummy(
                Selected_Option="$0-499",
                Selected_Option2="1-2 weeks",
                RC_zero_to_499=0,
                RC_500_to_999=0,
                RC_1000_to_2499=0,
                RC_2500_to_4999=0,
                RC_5000_to_9999=0,
                RC_10000_to_24999=0,
                RC_25000_to_49999=0,
                RC_More_Than_50000=0,
                RT_1D_to_1W=0,
                RT_1W_to_2W=0,
                RT_2W_to_4W=0,
                RT_1M_to_2M=0,
                RT_2M_to_3M=0,
                RT_3M_to_6M=0,
                RT_6M_to_12M=0,
                RT_More_Than_a_Year=0,
            )

            # EQuestions1 (stage)
            m_eq1.objects.get.return_value = Dummy(
                Idea=1,
                Formation=0,
                Start_Up=0,
                Growth=0,
                M_And_A=0,
                Preparing_For_Public=0,
                Distressed=0,
                Selected_Option="Idea",
            )

            # EQuestions2 (entity)
            m_eq2.objects.get.return_value = Dummy(
                Business_Name="ACME Inc",
                Selected_Option="LLC",
                Registration_Region="NV",
            )

            # EQuestions3 (pre-capital)
            m_eq3.objects.get.return_value = Dummy(
                Selected_Option="<$25k",
                Less_25k=1,
                More_25K_Less_100k=0,
                More_100k_Less_250K=0,
                More_250k_Less_500K=0,
                More_500K_Less_1M=0,
                More_1M_Less_2M=0,
                More_2M_Less_5M=0,
                More_5M_Less_10M=0,
                More_10M=0,
            )

            # EQuestions4 (pre-market types)
            m_eq4.objects.get.return_value = Dummy(
                Selected_Options=["Accelerator", "Bonds"],
                Accelerator=1,
                Bonds=1,
                Comercial_Banking=0,
                Cryptocurrency=0,
                EB5_Immigration=0,
                Enterprise_Zones=0,
                Factoring=0,
                Grants=0,
                Hedge_Funds=0,
                Incubator=0,
                Investment_Banking=0,
                Other_Owner_Equity=0,
                Private_Debt=0,
                Private_Equity=0,
                Public_Offereing=0,
                Real_Estate=0,
                Royalty_Financing=0,
                Small_Business_Administration=0,
                Venture_Capital=0,
                Unsure=0,
            )

            # EQuestions5 (planned raise)
            m_eq5.objects.get.return_value = Dummy(
                Selected_Option="$25k-$100k",
                Less_25k=0,
                More_25K_Less_100k=1,
                More_100k_Less_250K=0,
                More_250k_Less_500K=0,
                More_500K_Less_1M=0,
                More_1M_Less_1_35M=0,
                More_1_35M_Less_2M=0,
                More_2M_Less_5M=0,
                More_5M_Less_10M=0,
                More_10M_Less_20M=0,
                More_20M=0,
                Unsure=0,
            )

            # EQuestions6 (rounds)
            m_eq6.objects.get.return_value = Dummy(
                Selected_Options=["Seed"],
                Selected_Option=1,
                Founders_Round=0,
                Pre_Seed=0,
                Seed=1,
                Series_A=0,
                Series_B=0,
                Series_C=0,
                Pre_Ipo=0,
                Ipo=0,
                Unsure=0,
                One=1,
                Two=0,
                TBD=0,
            )

            # EQuestions7 (use of funds)
            m_eq7.objects.get.return_value = Dummy(
                Selected_Options=["Start_Up"],
                Start_Up=1,
                Growth_Scalabitlity=0,
                Marketing_and_Sales=0,
                Cash_FLow_Capital=0,
                Human_Capital=0,
                Equipment=0,
                Merger_and_Acquistions=0,
                Inventory=0,
                Real_State=0,
                Other=0,
                Unsure=0,
            )

            # EQuestions8 (risk)
            m_eq8.objects.get.return_value = Dummy(
                Selected_Option="Low",
                Selected_Option2="Medium",
                Low_Risk_Tolerance=1,
                Medium_Risk_Tolerance=0,
                High_Risk_Tolerance=0,
                Low_Cost_Capital=1,
                Medium_Cost_Capital=0,
                High_Cost_Capital=0,
                Very_High_Cost_Capital=0,
                Immaterial_Cost_Capital=0,
            )

            # Documents prepared
            m_docs.objects.get.return_value = Dummy(
                summary_of_offering="yes",
                financial_forecast="yes",
                lean_business_model="yes",
                presentation_deck="yes",
                leadership_overview="yes",
                exit_strategy="yes",
                offering_documents="yes",
                ai_generated_deep_dive="yes",
                virtual_data_room="yes",
            )

            # Import the view under test after patches are set
            from Matching_Algorithm.views import Match

            response = Match(request)
            self.assertEqual(response.status_code, 200)


