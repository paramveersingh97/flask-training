from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)  # here dump_only = True means that this field is created by us, we are not grtting it from the request
    name = fields.Str(required=True) 
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainTagSchema(Schema):
    id = fields.Int(dump_only = True)
    name = fields.Str()


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

class ItemSchema(PlainItemSchema): # inherit PlainItemSchema
    store_id = fields.Int(Required=True, load_only= True) # load_only => whenever we use ItemSchema, we're  gonna be able to pass in the store_id when we're receiving data from the client
    store = fields.Nested(PlainStoreSchema(), dump_only = True)

class StoreSchema(PlainStoreSchema):
    items = fields.Nested(PlainItemSchema(), dump_only= True)
    tags = fields.Nested(PlainTagSchema(), dump_only= True)

class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only= True)
    store = fields.Nested(PlainStoreSchema(), dump_only = True)


