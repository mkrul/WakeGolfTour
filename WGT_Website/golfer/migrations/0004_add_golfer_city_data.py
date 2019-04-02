from django.db import migrations
import csv 

class Migration(migrations.Migration):

    dependencies = [ 
        ('golfer', '0003_add_golfer_city'),
    ]   

    operations = [ 
    ]   

    def add_city_data(apps, schema_editor):
        file = open('golfersInput.csv', 'r')
        csvReader = csv.reader(file)
        golfers = list(csvReader)
        ([each.strip for each in row] for row in golfers)
        file.close()

        Golfer = apps.get_model('golfer', 'Golfer')
        for name, bdate, city in golfers:
            golfer = Golfer.objects.get(golfer_name=name)
            golfer.golfer_city = city
            golfer.save()
           
    def remove_city_data(apps, schema_editor):
        Golfer = apps.get_model('golfer', 'Golfer')
        Golfer.object.update(golfer_city='unknown')
        operations = [
            migrations.RunPython(add_city_data, reverse_code=remove_city_data)
        ]

