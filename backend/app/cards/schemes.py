from marshmallow import Schema, fields


class CardSchema(Schema):
    card_id = fields.Int(required=True)
    title = fields.Str(required=True)
    image = fields.Str(required=True)
    price_min = fields.Int(required=True)
    price_max = fields.Int(required=True)
    genre_title = fields.Str(required=True)
    genre_name = fields.Str(required=True)
    location = fields.Str(required=True)
    address = fields.Str(required=True)
    is_pushkins_card = fields.Bool(required=True)
    details = fields.Str(required=True)
    description = fields.Str(required=True)


class CardListResponseSchema(Schema):
    cards = fields.Nested(CardSchema, many=True)
