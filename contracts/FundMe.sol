// SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;

contract FundMe {
    function fund() public payable {
        require(msg.value>=1, "Didn't send enough");
    }

    function withdraw() private{

    }
}