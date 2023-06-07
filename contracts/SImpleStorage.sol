// SPDX-License-Identifier: MIT
pragma solidity >=0.8.8;

contract SimpleStorage {
    uint256 public  number;

    function getNumber (uint256 _number) public {
        number = _number;
    }
}

//0xd9145CCE52D386f254917e481eB44e9943F39138 address of contract