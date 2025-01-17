# EzdoctemplatedocumentGetObjectV2Response

Response for GET /2/object/ezdoctemplatedocument/{pkiEzdoctemplatedocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzdoctemplatedocumentGetObjectV2ResponseMPayload**](EzdoctemplatedocumentGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_get_object_v2_response import EzdoctemplatedocumentGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentGetObjectV2Response from a JSON string
ezdoctemplatedocument_get_object_v2_response_instance = EzdoctemplatedocumentGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentGetObjectV2Response.to_json())

# convert the object into a dict
ezdoctemplatedocument_get_object_v2_response_dict = ezdoctemplatedocument_get_object_v2_response_instance.to_dict()
# create an instance of EzdoctemplatedocumentGetObjectV2Response from a dict
ezdoctemplatedocument_get_object_v2_response_from_dict = EzdoctemplatedocumentGetObjectV2Response.from_dict(ezdoctemplatedocument_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


