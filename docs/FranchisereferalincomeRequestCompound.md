# FranchisereferalincomeRequestCompound

A Franchisereferalincome Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_contact** | [**[ContactRequestCompound]**](ContactRequestCompound.md) |  | 
**fki_franchisebroker_id** | **int** | The unique ID of the Franchisebroker | 
**fki_franchisereferalincomeprogram_id** | **int** | The unique ID of the Franchisereferalincomeprogram | 
**fki_period_id** | **int** | The unique ID of the Period | 
**d_franchisereferalincome_loan** | **str** | The loan amount | 
**d_franchisereferalincome_franchiseamount** | **str** | The amount that will be given to the franchise | 
**d_franchisereferalincome_franchisoramount** | **str** | The amount that will be kept by the franchisor | 
**d_franchisereferalincome_agentamount** | **str** | The amount that will be given to the agent | 
**dt_franchisereferalincome_disbursed** | **str** | The date the amounts were disbursed | 
**t_franchisereferalincome_comment** | **str** | A comment about the transaction | 
**fki_franchiseoffice_id** | **int** | The unique ID of the Franchisereoffice | 
**s_franchisereferalincome_remoteid** | **str** |  | 
**obj_address** | [**AddressRequest**](AddressRequest.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


