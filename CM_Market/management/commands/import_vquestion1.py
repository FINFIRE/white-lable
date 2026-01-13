import pandas as pd
from django.core.management.base import BaseCommand
from CM_Market.models import VQuestion1, UserDetail

class Command(BaseCommand):
    help = 'Import VQuestion1 data from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('Finfire/required_data_uncleaned/database_iterations_after_prototype/3c.xlsx', type=str, help='The path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['Finfire/required_data_uncleaned/database_iterations_after_prototype/3c.xlsx']

        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path,header=0)

        for _, row in df.iterrows():
            # Retrieve or create related UserDetail instance if needed
            user_detail = None
            if 'user_id' in df.columns:
                user_detail = UserDetail.objects.filter(unique_id=row['user_id']).first()

            # Create a new VQuestion1 instance
            vquestion1 = VQuestion1(
                user=user_detail,
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
                CM_Type=row['CM_Type']
            )
            vquestion1.save()
            self.stdout.write(self.style.SUCCESS(f"Added {vquestion1.First_Name} {vquestion1.Last_Name}"))

        self.stdout.write(self.style.SUCCESS('Import completed successfully!'))
