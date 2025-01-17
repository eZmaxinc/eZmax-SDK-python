# EzdoctemplatedocumentGetListV1Response

Response for GET /1/object/ezdoctemplatedocument/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzdoctemplatedocumentGetListV1ResponseMPayload**](EzdoctemplatedocumentGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_get_list_v1_response import EzdoctemplatedocumentGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentGetListV1Response from a JSON string
ezdoctemplatedocument_get_list_v1_response_instance = EzdoctemplatedocumentGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentGetListV1Response.to_json())

# convert the object into a dict
ezdoctemplatedocument_get_list_v1_response_dict = ezdoctemplatedocument_get_list_v1_response_instance.to_dict()
# create an instance of EzdoctemplatedocumentGetListV1Response from a dict
ezdoctemplatedocument_get_list_v1_response_from_dict = EzdoctemplatedocumentGetListV1Response.from_dict(ezdoctemplatedocument_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


