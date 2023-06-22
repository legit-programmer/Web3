// SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    

    uint256 public constant MIN_USD = 50*1e18;
    address[] public funders;
    mapping(address=>uint256) public amounts;
    address public immutable owner;
    error NotOwner();
    AggregatorV3Interface public priceFeed;
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }

    function getPrice() internal view returns (uint256) {
        
        (
            /* uint80 roundID */,
            int answer,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = priceFeed.latestRoundData();

        return uint256(answer*1e10);
    }

    function getConversionRate(uint256 amountInEth) internal view returns (uint256) {
        return ((amountInEth*getPrice())/1e18);
    }
    

    function fund() public payable {
        require(getConversionRate(msg.value)>=MIN_USD, "Didn't send enough");
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

    receive()  external payable {
        fund();
    }

    fallback() external payable {
        fund();
    }
}