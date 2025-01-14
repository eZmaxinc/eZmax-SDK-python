# EzdoctemplatetypeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/ezdoctemplatetype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezdoctemplatetype** | [**List[EzdoctemplatetypeAutocompleteElementResponse]**](EzdoctemplatetypeAutocompleteElementResponse.md) | An array of Ezdoctemplatetype autocomplete element response. | 

## Example

```python
from eZmaxApi.models.ezdoctemplatetype_get_autocomplete_v2_response_m_payload import EzdoctemplatetypeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatetypeGetAutocompleteV2ResponseMPayload from a JSON string
ezdoctemplatetype_get_autocomplete_v2_response_m_payload_instance = EzdoctemplatetypeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatetypeGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
ezdoctemplatetype_get_autocomplete_v2_response_m_payload_dict = ezdoctemplatetype_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of EzdoctemplatetypeGetAutocompleteV2ResponseMPayload from a dict
ezdoctemplatetype_get_autocomplete_v2_response_m_payload_from_dict = EzdoctemplatetypeGetAutocompleteV2ResponseMPayload.from_dict(ezdoctemplatetype_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


