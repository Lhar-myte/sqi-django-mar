class Migration(migrations.Migration):
 
     dependencies = [
         ('coffeeshop', '0002_alter_order_total_price'),
     ]
 
     operations = [
         migrations.RemoveField(
             model_name='order',
             name='total_price',
         ),
     ]