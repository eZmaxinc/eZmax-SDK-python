# EzdoctemplatedocumentGetListV1ResponseMPayload

Payload for GET /1/object/ezdoctemplatedocument/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezdoctemplatedocument** | [**List[EzdoctemplatedocumentListElement]**](EzdoctemplatedocumentListElement.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_get_list_v1_response_m_payload import EzdoctemplatedocumentGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentGetListV1ResponseMPayload from a JSON string
ezdoctemplatedocument_get_list_v1_response_m_payload_instance = EzdoctemplatedocumentGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentGetListV1ResponseMPayload.to_json())

# convert the object into a dict
ezdoctemplatedocument_get_list_v1_response_m_payload_dict = ezdoctemplatedocument_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of EzdoctemplatedocumentGetListV1ResponseMPayload from a dict
ezdoctemplatedocument_get_list_v1_response_m_payload_from_dict = EzdoctemplatedocumentGetListV1ResponseMPayload.from_dict(ezdoctemplatedocument_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


