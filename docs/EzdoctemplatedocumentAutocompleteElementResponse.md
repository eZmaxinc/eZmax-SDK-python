# EzdoctemplatedocumentAutocompleteElementResponse

A Ezdoctemplatedocument AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | 
**s_ezdoctemplatedocument_name_x** | **str** | The name of the Ezdoctemplatedocument in the language of the requester | 
**b_ezdoctemplatedocument_isactive** | **bool** | Whether the ezdoctemplatedocument is active or not | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_autocomplete_element_response import EzdoctemplatedocumentAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentAutocompleteElementResponse from a JSON string
ezdoctemplatedocument_autocomplete_element_response_instance = EzdoctemplatedocumentAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentAutocompleteElementResponse.to_json())

# convert the object into a dict
ezdoctemplatedocument_autocomplete_element_response_dict = ezdoctemplatedocument_autocomplete_element_response_instance.to_dict()
# create an instance of EzdoctemplatedocumentAutocompleteElementResponse from a dict
ezdoctemplatedocument_autocomplete_element_response_from_dict = EzdoctemplatedocumentAutocompleteElementResponse.from_dict(ezdoctemplatedocument_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


