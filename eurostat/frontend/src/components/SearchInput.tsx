import { tab } from "@testing-library/user-event/dist/tab";
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const SearchInput = () => {
  const [tableSelected, setTableSelected] = useState("");
  const [search, setSearch] = useState("");
  const handleSearch = (e: any) => {
    setSearch(e.target.value);
  };

  const [values, setValues] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const delayDebounceFn = setTimeout(() => {
      fetch(
        process.env.REACT_APP_DOMAIN +
          "/search/?q=" +
          search +
          "&table=" +
          tableSelected
      )
        .then((res) => {
          return res.json();
        })
        .then((data: any) => {
          setValues(data.map((d: any) => d.location));
        })
        .catch((err) => {
          console.log("an error has happened", err);
        });
    }, 1000);

    return () => clearTimeout(delayDebounceFn);
  }, [search]);

  const goToSearchResult = (value: any) => {};

  const handleSubmit = () => {
    navigate("/search-results", {
      state: {
        data: {
          table: tableSelected,
          query: search,
        },
      },
    });
  };
  return (
    <div className="w-full">
      <form onSubmit={handleSubmit}>
        <div>
          <label
            htmlFor="countries"
            className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >
            Select an option
          </label>
          <select
            id="countries"
            onChange={(e) => setTableSelected(e.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
            mb-5 w-40 m-auto    "
          >
            <option selected={"" === tableSelected}>
              Choose a Table to query:
            </option>
            <option value={"housing"} selected={"housing" === tableSelected}>
              Housing
            </option>
            <option value={"job"} selected={"job" === tableSelected}>
              Job
            </option>
            <option value={"consumer"} selected={"consumer" === tableSelected}>
              Consumer
            </option>
          </select>
        </div>
        <div>
          <label
            htmlFor="default-search"
            className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
          >
            Search
          </label>
          <div className="relative">
            <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg
                aria-hidden="true"
                className="w-5 h-5 text-gray-500 dark:text-gray-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                ></path>
              </svg>
            </div>
            <input
              type="search"
              id="default-search"
              className="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Search Mockups, Logos..."
              required
              value={search}
              onChange={handleSearch}
            />
            <button
              type="submit"
              className="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Search
            </button>
          </div>
        </div>
        {values.length > 0 && (
          <ul className="container overflow-scroll bg-white z-20 p-8">
            {values.map((value) => {
              return (
                <li
                  className="text-center text-black border-b-2 border-black hover:cursor-pointer"
                  onClick={() => goToSearchResult(value)}
                >
                  {value}
                </li>
              );
            })}
          </ul>
        )}
      </form>
    </div>
  );
};

export default SearchInput;
