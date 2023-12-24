# AttemptResponseCompound

An Attempt object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_attempt_start** | **str** | Represent a Date Time. The timezone is the one configured in the User&#39;s profile. | 
**s_attempt_result** | **str** | The Success or Failure message of the attempt when we tried to call the URL to deliver the webhook event. | 
**i_attempt_duration** | **int** | The number of second it took to process the webhook or get an error | 

## Example

```python
from eZmaxApi.models.attempt_response_compound import AttemptResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of AttemptResponseCompound from a JSON string
attempt_response_compound_instance = AttemptResponseCompound.from_json(json)
# print the JSON string representation of the object
print AttemptResponseCompound.to_json()

# convert the object into a dict
attempt_response_compound_dict = attempt_response_compound_instance.to_dict()
# create an instance of AttemptResponseCompound from a dict
attempt_response_compound_form_dict = attempt_response_compound.from_dict(attempt_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


