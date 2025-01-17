# EzdoctemplatedocumentCreateObjectV1Response

Response for POST /1/object/ezdoctemplatedocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzdoctemplatedocumentCreateObjectV1ResponseMPayload**](EzdoctemplatedocumentCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_create_object_v1_response import EzdoctemplatedocumentCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentCreateObjectV1Response from a JSON string
ezdoctemplatedocument_create_object_v1_response_instance = EzdoctemplatedocumentCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentCreateObjectV1Response.to_json())

# convert the object into a dict
ezdoctemplatedocument_create_object_v1_response_dict = ezdoctemplatedocument_create_object_v1_response_instance.to_dict()
# create an instance of EzdoctemplatedocumentCreateObjectV1Response from a dict
ezdoctemplatedocument_create_object_v1_response_from_dict = EzdoctemplatedocumentCreateObjectV1Response.from_dict(ezdoctemplatedocument_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


