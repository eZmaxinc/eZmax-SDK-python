# EzdoctemplatedocumentEditObjectV1Response

Response for PUT /1/object/ezdoctemplatedocument/{pkiEzdoctemplatedocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_edit_object_v1_response import EzdoctemplatedocumentEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentEditObjectV1Response from a JSON string
ezdoctemplatedocument_edit_object_v1_response_instance = EzdoctemplatedocumentEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentEditObjectV1Response.to_json())

# convert the object into a dict
ezdoctemplatedocument_edit_object_v1_response_dict = ezdoctemplatedocument_edit_object_v1_response_instance.to_dict()
# create an instance of EzdoctemplatedocumentEditObjectV1Response from a dict
ezdoctemplatedocument_edit_object_v1_response_from_dict = EzdoctemplatedocumentEditObjectV1Response.from_dict(ezdoctemplatedocument_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


