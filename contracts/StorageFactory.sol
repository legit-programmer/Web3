// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "contracts/SImpleStorage.sol";

contract StorageFactory {
    SimpleStorage[] public _storage;
    function createStorage() public {
        _storage.push(new SimpleStorage());
    }

    function store(uint256 index, uint256 number) public {
        SimpleStorage tempStorage = _storage[index];
        tempStorage.storeNumber(number);
    }

    function get(uint256 index) view public returns(uint256) {
        // return storage's number
        SimpleStorage temp = _storage[index];
        return temp.retrieve();
        
    }


}