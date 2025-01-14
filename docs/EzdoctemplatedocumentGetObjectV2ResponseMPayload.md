# EzdoctemplatedocumentGetObjectV2ResponseMPayload

Payload for GET /2/object/ezdoctemplatedocument/{pkiEzdoctemplatedocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezdoctemplatedocument** | [**EzdoctemplatedocumentResponseCompound**](EzdoctemplatedocumentResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_get_object_v2_response_m_payload import EzdoctemplatedocumentGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentGetObjectV2ResponseMPayload from a JSON string
ezdoctemplatedocument_get_object_v2_response_m_payload_instance = EzdoctemplatedocumentGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezdoctemplatedocument_get_object_v2_response_m_payload_dict = ezdoctemplatedocument_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzdoctemplatedocumentGetObjectV2ResponseMPayload from a dict
ezdoctemplatedocument_get_object_v2_response_m_payload_from_dict = EzdoctemplatedocumentGetObjectV2ResponseMPayload.from_dict(ezdoctemplatedocument_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


