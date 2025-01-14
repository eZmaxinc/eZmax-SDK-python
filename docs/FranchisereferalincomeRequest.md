# FranchisereferalincomeRequest

An Franchisereferalincome Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_franchisereferalincome_id** | **int** | The unique ID of the Franchisereferalincome | [optional] 
**fki_franchisebroker_id** | **int** | The unique ID of the Franchisebroker | 
**fki_franchisereferalincomeprogram_id** | **int** | The unique ID of the Franchisereferalincomeprogram | 
**fki_period_id** | **int** | The unique ID of the Period | 
**d_franchisereferalincome_loan** | **str** | The loan amount | 
**d_franchisereferalincome_franchiseamount** | **str** | The amount that will be given to the franchise | 
**d_franchisereferalincome_franchisoramount** | **str** | The amount that will be kept by the franchisor | 
**d_franchisereferalincome_agentamount** | **str** | The amount that will be given to the agent | 
**dt_franchisereferalincome_disbursed** | **str** | The date the amounts were disbursed | 
**t_franchisereferalincome_comment** | **str** | Comment about the transaction | 
**fki_franchiseoffice_id** | **int** | The unique ID of the Franchisereoffice | 
**s_franchisereferalincome_remoteid** | **str** |  | 

## Example

```python
from eZmaxApi.models.franchisereferalincome_request import FranchisereferalincomeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FranchisereferalincomeRequest from a JSON string
franchisereferalincome_request_instance = FranchisereferalincomeRequest.from_json(json)
# print the JSON string representation of the object
print(FranchisereferalincomeRequest.to_json())

# convert the object into a dict
franchisereferalincome_request_dict = franchisereferalincome_request_instance.to_dict()
# create an instance of FranchisereferalincomeRequest from a dict
franchisereferalincome_request_from_dict = FranchisereferalincomeRequest.from_dict(franchisereferalincome_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


