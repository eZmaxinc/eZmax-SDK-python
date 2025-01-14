# EzdoctemplatetypeAutocompleteElementResponse

A Ezdoctemplatetype AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezdoctemplatetype_id** | **int** | The unique ID of the Ezdoctemplatetype | 
**s_ezdoctemplatetype_description_x** | **str** | The description of the Ezdoctemplatetype in the language of the requester | 
**b_ezdoctemplatetype_isactive** | **bool** | Whether the Ezdoctemplatetype is active or not | 

## Example

```python
from eZmaxApi.models.ezdoctemplatetype_autocomplete_element_response import EzdoctemplatetypeAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatetypeAutocompleteElementResponse from a JSON string
ezdoctemplatetype_autocomplete_element_response_instance = EzdoctemplatetypeAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatetypeAutocompleteElementResponse.to_json())

# convert the object into a dict
ezdoctemplatetype_autocomplete_element_response_dict = ezdoctemplatetype_autocomplete_element_response_instance.to_dict()
# create an instance of EzdoctemplatetypeAutocompleteElementResponse from a dict
ezdoctemplatetype_autocomplete_element_response_from_dict = EzdoctemplatetypeAutocompleteElementResponse.from_dict(ezdoctemplatetype_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


