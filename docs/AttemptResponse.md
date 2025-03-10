# AttemptResponse

An Attempt object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_attempt_start** | **str** | Represent a Date Time. The timezone is the one configured in the User&#39;s profile. | 
**s_attempt_result** | **str** | The Success or Failure message of the attempt when we tried to call the URL to deliver the webhook event. | 
**i_attempt_duration** | **int** | The number of second it took to process the webhook or get an error | 

## Example

```python
from eZmaxApi.models.attempt_response import AttemptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttemptResponse from a JSON string
attempt_response_instance = AttemptResponse.from_json(json)
# print the JSON string representation of the object
print(AttemptResponse.to_json())

# convert the object into a dict
attempt_response_dict = attempt_response_instance.to_dict()
# create an instance of AttemptResponse from a dict
attempt_response_from_dict = AttemptResponse.from_dict(attempt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


