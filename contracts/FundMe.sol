// SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    uint256 minUSD = 50;
    AggregatorV3Interface internal priceFeed;
    address[] public funders;
    mapping(address=>uint256) amounts;

    constructor() {
        priceFeed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
    } 

    function fund() public payable {
        require(getConversionRate(msg.value)>=minUSD, "Didn't send enough");
        funders.push(msg.sender);
        amounts[msg.sender] = msg.value;
    }

    function getPrice() public view returns (uint256) {
        (
            /* uint80 roundID */,
            int answer,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = priceFeed.latestRoundData();

        return uint256(answer*1e10);
    }

    function getConversionRate(uint256 amountInEth) public view returns (uint256) {
        return ((amountInEth*getPrice())/1e18);
    }
    function withdraw() private{

    }
}