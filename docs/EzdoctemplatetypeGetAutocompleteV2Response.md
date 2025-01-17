# EzdoctemplatetypeGetAutocompleteV2Response

Response for GET /2/object/ezdoctemplatetype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzdoctemplatetypeGetAutocompleteV2ResponseMPayload**](EzdoctemplatetypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatetype_get_autocomplete_v2_response import EzdoctemplatetypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatetypeGetAutocompleteV2Response from a JSON string
ezdoctemplatetype_get_autocomplete_v2_response_instance = EzdoctemplatetypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatetypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
ezdoctemplatetype_get_autocomplete_v2_response_dict = ezdoctemplatetype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of EzdoctemplatetypeGetAutocompleteV2Response from a dict
ezdoctemplatetype_get_autocomplete_v2_response_from_dict = EzdoctemplatetypeGetAutocompleteV2Response.from_dict(ezdoctemplatetype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


