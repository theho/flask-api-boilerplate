from marshmallow import Schema, fields


class UserSignUpSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    password = fields.Str(required=True)

    # type = fields.Str(required=True)


#
#
# class UserSchema(Schema):
#     id = fields.Int(dump_only=True)
#
#     username = fields.Str(required=True, dump_only=True)
#     email = fields.Email(required=True, dump_only=True)
#
#     first_name = fields.Str(required=True)
#     last_name = fields.Str(required=True)
#
#     roles = fields.List(fields.String, required=True, dump_only=True)
#     created_at = fields.DateTime(dump_only=True, required=True)
#
#
# class TokenSchema(Schema):
#     token = fields.Str(dump_only=True)
#
#
# user_schema = UserSchema(strict=True)
# public_user_schema = UserSchema(strict=True, only=('profile', 'first_name', 'username',))
signup_schema = UserSignUpSchema(strict=True)
#
# token_schema = TokenSchema(strict=True)
