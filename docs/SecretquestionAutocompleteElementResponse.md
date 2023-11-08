# SecretquestionAutocompleteElementResponse

A Secretquestion AutocompleteElement Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_secretquestion_text_x** | **str** | The text of the Secretquestion in the language of the requester | 
**pki_secretquestion_id** | **int** | The unique ID of the Secretquestion.  Valid values:  |Value|Description| |-|-| |1|The name of the hospital in which you were born| |2|The name of your grade school| |3|The last name of your favorite teacher| |4|Your favorite sports team| |5|Your favorite TV show| |6|Your favorite movie| |7|The name of the street on which you grew up| |8|The name of your first employer| |9|Your first car| |10|Your favorite food| |11|The name of your first pet| |12|Favorite musician/band| |13|What instrument you play| |14|Your father&#39;s middle name| |15|Your mother&#39;s maiden name| |16|Name of your eldest child| |17|Your spouse&#39;s middle name| |18|Favorite restaurant| |19|Childhood nickname| |20|Favorite vacation destination| |21|Your boat&#39;s name| |22|Date of Birth (YYYY-MM-DD)| |22|Secret Code| |22|Your reference code| | 
**b_secretquestion_isactive** | **bool** | Whether the Secretquestion is active or not | 

## Example

```python
from eZmaxApi.models.secretquestion_autocomplete_element_response import SecretquestionAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecretquestionAutocompleteElementResponse from a JSON string
secretquestion_autocomplete_element_response_instance = SecretquestionAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print SecretquestionAutocompleteElementResponse.to_json()

# convert the object into a dict
secretquestion_autocomplete_element_response_dict = secretquestion_autocomplete_element_response_instance.to_dict()
# create an instance of SecretquestionAutocompleteElementResponse from a dict
secretquestion_autocomplete_element_response_form_dict = secretquestion_autocomplete_element_response.from_dict(secretquestion_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


