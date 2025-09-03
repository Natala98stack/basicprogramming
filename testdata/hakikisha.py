records=[{'name': 'Collins Natala', 'id_number': '60535060', 'phone_number': '0788591334'}, {'name': 'Amina Wanjiku', 'id_number': '15209062', 'phone_number': '0791632404'}, {'name': 'Brian Otieno', 'id_number': '91872954', 'phone_number': '0775717858'}, {'name': 'Faith Mwangi', 'id_number': '94689840', 'phone_number': '0777554534'}, {'name': 'Kevin Kiptoo', 'id_number': '25235801', 'phone_number': '0740610914'}, {'name': 'Lilian Njeri', 'id_number': '56996184', 'phone_number': '0781444694'}]
def hakikisha(phone_number, id_number):

    found=False
    name=""
    for record in records:

        if phone_number==record["phone_number"] and id_number==record["id_number"]:
            print(record)
            found=True
            name=record["name"]
    return {"found":found, "name":name}
result=hakikisha(phone_number="0788591334", id_number="60535060")
print(result)