# EzdoctemplatefieldtypecategoryAutocompleteElementResponse

A Ezdoctemplatefieldtypecategory AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezdoctemplatefieldtypecategory_id** | **int** | The unique ID of the Ezdoctemplatefieldtypecategory | 
**fki_ezdoctemplatetype_id** | **int** | The unique ID of the Ezdoctemplatetype | 
**s_ezdoctemplatefieldtypecategory_description_x** | **str** | The description of the Ezdoctemplatefieldtypecategory in the language of the requester | 
**b_ezdoctemplatefieldtypecategory_isactive** | **bool** | Whether the Ezdoctemplatefieldtypecategory is active or not | 

## Example

```python
from eZmaxApi.models.ezdoctemplatefieldtypecategory_autocomplete_element_response import EzdoctemplatefieldtypecategoryAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatefieldtypecategoryAutocompleteElementResponse from a JSON string
ezdoctemplatefieldtypecategory_autocomplete_element_response_instance = EzdoctemplatefieldtypecategoryAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatefieldtypecategoryAutocompleteElementResponse.to_json())

# convert the object into a dict
ezdoctemplatefieldtypecategory_autocomplete_element_response_dict = ezdoctemplatefieldtypecategory_autocomplete_element_response_instance.to_dict()
# create an instance of EzdoctemplatefieldtypecategoryAutocompleteElementResponse from a dict
ezdoctemplatefieldtypecategory_autocomplete_element_response_from_dict = EzdoctemplatefieldtypecategoryAutocompleteElementResponse.from_dict(ezdoctemplatefieldtypecategory_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


