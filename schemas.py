from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True)  # here dump_only = True means that this field is created by us, we are not grtting it from the request
    name = fields.Str(required=True) 
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)