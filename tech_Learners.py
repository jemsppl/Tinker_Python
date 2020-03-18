fld= "test"
fields = open('field.txt','w')
field_list = fields
if fld not in field_list:
    field_list.append(fld)
with open('field.txt','w') as f:
    f.write(field_list)
