
 from django.db import migrations, models
 
 
 class Migration(migrations.Migration):
 
     dependencies = [
         ('coffeeshop', '0003_remove_order_total_price'),
    ]
 
     operations = [
         migrations.AddField(
             model_name='order',
             name='total_order_price',
             field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
             preserve_default=False,
        ),
    ]