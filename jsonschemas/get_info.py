class GetInfo:
    def get_info(self):
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "profession": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "profession"
                    ]
                }
            ]
        }
        return schema
