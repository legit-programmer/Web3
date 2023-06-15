// SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;
import "contracts/PriceConverter.sol";

contract FundMe {
    using PriceConverter for uint256;

    uint256 public constant MIN_USD = 50*1e18;
    address[] public funders;
    mapping(address=>uint256) public amounts;
    address public immutable owner;
    error NotOwner();
    constructor() {
        owner = msg.sender;
    }
    

    function fund() public payable {
        require(msg.value.getConversionRate()>=MIN_USD, "Didn't send enough");
        funders.push(msg.sender);
        amounts[msg.sender] += msg.value;
    }

    
    function withdraw() public onlyOwner{
        
        for (uint256 i; i<funders.length;i++){
            address funder = funders[i];
            amounts[funder] = 0;
        }
        funders = new address[](0);

        // transfer throws error
        // payable(msg.sender).transfer(address(this).balance);

        // // send returns bool
        // bool transactionStatus = payable(msg.sender).send(address(this).balance);
        // require(transactionStatus, "Not sent");

        // call can call funtions
        (bool success,) = payable(msg.sender).call{value:address(this).balance}("");
        require(success, "Not sent");
    }

    modifier onlyOwner(){
        // require(msg.sender==owner, "You are not the owner lmao.");
        if(msg.sender!=owner){
            revert NotOwner();
        }
        _;
    }
}