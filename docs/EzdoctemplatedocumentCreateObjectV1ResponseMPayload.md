# EzdoctemplatedocumentCreateObjectV1ResponseMPayload

Payload for POST /1/object/ezdoctemplatedocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezdoctemplatedocument_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_create_object_v1_response_m_payload import EzdoctemplatedocumentCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentCreateObjectV1ResponseMPayload from a JSON string
ezdoctemplatedocument_create_object_v1_response_m_payload_instance = EzdoctemplatedocumentCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentCreateObjectV1ResponseMPayload.to_json())

# convert the object into a dict
ezdoctemplatedocument_create_object_v1_response_m_payload_dict = ezdoctemplatedocument_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of EzdoctemplatedocumentCreateObjectV1ResponseMPayload from a dict
ezdoctemplatedocument_create_object_v1_response_m_payload_from_dict = EzdoctemplatedocumentCreateObjectV1ResponseMPayload.from_dict(ezdoctemplatedocument_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


