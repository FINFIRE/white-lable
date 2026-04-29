import pandas as pd
from django.core.management.base import BaseCommand
from iquestions.models import IQuestions1, UserDetail

class Command(BaseCommand):
    help = 'Import IQuestion1 data from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('Finfire/Intermediaries_FINFIRE_Beta.xlsx', type=str, help='The path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['Finfire/Intermediaries_FINFIRE_Beta.xlsx']

        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path,header=0)

        for _, row in df.iterrows():
            # Retrieve or create related UserDetail instance if needed
            user_detail = None
            if 'user_id' in df.columns:
                user_detail = UserDetail.objects.filter(unique_id=row['user_id']).first()

            # Create a new VQuestion1 instance
            iquestion1 = IQuestions1(
                user=user_detail,
                Prefered_CM = row.get('Prefered_CM',""),
                Specialized_Industry = row.get('Specialized_Industry',""),
                Regions_Served = row.get('Regions_Served',""),
                Selected_Options = row.get('Selected_Options',""),
                First_Name=row['First_Name'],
                Last_Name=row['Last_Name'],
                Company_Name=row.get('Company_Name', ''),
                Primary_Phone=row.get('Primary_Phone', ''),
                Secondary_Phone=row.get('Secondary_Phone', ''),
                Alternate_Phone=row.get('Alternate_Phone', ''),
                Email=row.get('Email', ''),
                Adress=row.get('Adress', ''),
                City=row.get('City', ''),
                State=row.get('State',''),
                Zip_Code=row.get('Zip_Code', ''),
                I_Type=row['I_Type']
            )
            iquestion1.save()
            self.stdout.write(self.style.SUCCESS(f"Added {iquestion1.First_Name} {iquestion1.Last_Name}"))

        self.stdout.write(self.style.SUCCESS('Import completed successfully!'))
