import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";

const SearchResult = () => {
  const { state } = useLocation();
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  useEffect(() => {
    fetch(
      `http://sw.hackety.space:9999/search/?q=${state.data.query}&table=${state.data.table}`
    )
      .then((res) => res.json())
      .then((data: any) => {
        console.log(data);
        setData(data);
      })
      .catch((err) => {
        setError(err);
      });
  }, []);
  return (
    <div className="m-auto max-w-lg pt-32 ">
      <p>Search Results</p>
      {error ? (
        <h1>{error}</h1>
      ) : (
        <div className="relative overflow-scroll">
          <table className="w-full max-h-60 h-60 text-sm table-auto text-left text-gray-500 dark:text-gray-400 overflow-scroll">
            <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
              <tr>
                <th scope="col" className="px-6 py-3">
                  Location
                </th>
                <th scope="col" className="px-6 py-3">
                  Value
                </th>
                <th scope="col" className="px-6 py-3">
                  Quarter
                </th>
                <th scope="col" className="px-6 py-3">
                  Year
                </th>
              </tr>
            </thead>
            <tbody className="overflow-scroll">
              {data.map((d: any) => {
                return (
                  <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                    <td className="px-6 py-4">{d.location}</td>
                    <td className="px-6 py-4">{d.value}</td>
                    <td className="px-6 py-4">{d.quarter}</td>
                    <td className="px-6 py-4">{d.year}</td>
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
