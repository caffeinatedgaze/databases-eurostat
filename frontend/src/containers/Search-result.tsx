import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";

const SearchResult = () => {
  const { state } = useLocation();
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  useEffect(() => {
    fetch(
      `http://sw.hackety.space:9999/search/?q=${state.search}&table=${state.tableSelected}`
    )
      .then((res) => res.json())
      .then((data) => {
        setData(data);
      })
      .catch((err) => {
        setError(err);
      });
  }, []);
  return (
    <div className="m-auto max-w-lg pt-32">
      <p>Search Results</p>
      {error ? (
        <h1>{error}</h1>
      ) : (
        <div className="relative overflow-x-auto">
          <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
            <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
              <tr>
                <th scope="col" className="px-6 py-3">
                  Location
                </th>
                <th scope="col" className="px-6 py-3">
                  Value
                </th>
              </tr>
            </thead>
            <tbody>
              {data.map((d: any) => {
                return (
                  <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                    <td className="px-6 py-4">{d.location}</td>
                    <td className="px-6 py-4">{d.value}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default SearchResult;
