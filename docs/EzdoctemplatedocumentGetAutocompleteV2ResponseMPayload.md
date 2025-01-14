# EzdoctemplatedocumentGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezdoctemplatedocument/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezdoctemplatedocument** | [**List[EzdoctemplatedocumentAutocompleteElementResponse]**](EzdoctemplatedocumentAutocompleteElementResponse.md) | An array of Ezdoctemplatedocument autocomplete element response. | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_get_autocomplete_v2_response_m_payload import EzdoctemplatedocumentGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentGetAutocompleteV2ResponseMPayload from a JSON string
ezdoctemplatedocument_get_autocomplete_v2_response_m_payload_instance = EzdoctemplatedocumentGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
ezdoctemplatedocument_get_autocomplete_v2_response_m_payload_dict = ezdoctemplatedocument_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzdoctemplatedocumentGetAutocompleteV2ResponseMPayload from a dict
ezdoctemplatedocument_get_autocomplete_v2_response_m_payload_from_dict = EzdoctemplatedocumentGetAutocompleteV2ResponseMPayload.from_dict(ezdoctemplatedocument_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


