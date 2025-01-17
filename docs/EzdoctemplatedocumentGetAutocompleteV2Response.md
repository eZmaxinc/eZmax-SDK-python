# EzdoctemplatedocumentGetAutocompleteV2Response

Response for GET /2/object/ezdoctemplatedocument/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzdoctemplatedocumentGetAutocompleteV2ResponseMPayload**](EzdoctemplatedocumentGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_get_autocomplete_v2_response import EzdoctemplatedocumentGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentGetAutocompleteV2Response from a JSON string
ezdoctemplatedocument_get_autocomplete_v2_response_instance = EzdoctemplatedocumentGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentGetAutocompleteV2Response.to_json())

# convert the object into a dict
ezdoctemplatedocument_get_autocomplete_v2_response_dict = ezdoctemplatedocument_get_autocomplete_v2_response_instance.to_dict()
# create an instance of EzdoctemplatedocumentGetAutocompleteV2Response from a dict
ezdoctemplatedocument_get_autocomplete_v2_response_from_dict = EzdoctemplatedocumentGetAutocompleteV2Response.from_dict(ezdoctemplatedocument_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


