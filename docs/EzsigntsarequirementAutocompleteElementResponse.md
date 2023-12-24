# EzsigntsarequirementAutocompleteElementResponse

A Ezsigntsarequirement AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezsigntsarequirement_description_x** | **str** | The description of the Ezsigntsarequirement in the language of the requester | 
**pki_ezsigntsarequirement_id** | **int** | The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server&#39;s time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server&#39;s time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**| | 
**b_ezsigntsarequirement_isactive** | **bool** | Whether the Ezsigntsarequirement is active or not | 
**b_disabled** | **bool** | Indicates if the element is disabled in the context | 

## Example

```python
from eZmaxApi.models.ezsigntsarequirement_autocomplete_element_response import EzsigntsarequirementAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntsarequirementAutocompleteElementResponse from a JSON string
ezsigntsarequirement_autocomplete_element_response_instance = EzsigntsarequirementAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print EzsigntsarequirementAutocompleteElementResponse.to_json()

# convert the object into a dict
ezsigntsarequirement_autocomplete_element_response_dict = ezsigntsarequirement_autocomplete_element_response_instance.to_dict()
# create an instance of EzsigntsarequirementAutocompleteElementResponse from a dict
ezsigntsarequirement_autocomplete_element_response_form_dict = ezsigntsarequirement_autocomplete_element_response.from_dict(ezsigntsarequirement_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


