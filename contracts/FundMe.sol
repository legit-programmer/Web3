// SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;
import "contracts/PriceConverter.sol";

contract FundMe {
    using PriceConverter for uint256;

    uint256 minUSD = 50;
    address[] public funders;
    mapping(address=>uint256) amounts;

    

    function fund() public payable {
        require(msg.value.getConversionRate()>=minUSD, "Didn't send enough");
        funders.push(msg.sender);
        amounts[msg.sender] = msg.value;
    }

    
    function withdraw() private{

    }
}