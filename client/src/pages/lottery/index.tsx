import React, { useEffect, useState } from "react";

type LotteryNumber = {
  id: number;
  game_name: string;
  draw_date: string;
  draw_time: string;
  numbers: string;
  created_at: string;
};

function Lottery() {
  const [data, setData] = useState<{ lottery_numbers: LotteryNumber[] } | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    fetch("/api/lottery")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Lottery Page</h1>
      <table className="min-w-full bg-white border border-gray-200">
      <thead>
        <tr>
        <th className="py-2 px-4 border-b">Game</th>
        <th className="py-2 px-4 border-b">Date</th>
        <th className="py-2 px-4 border-b">Time</th>
        <th className="py-2 px-4 border-b">Numbers</th>
        <th className="py-2 px-4 border-b">Created At</th>
        </tr>
      </thead>
      <tbody>
        {data?.lottery_numbers.map((number) => (
        <tr key={number.id}>
          <td className="py-2 px-4 border-b">{number.game_name}</td>
          <td className="py-2 px-4 border-b">{number.draw_date}</td>
          <td className="py-2 px-4 border-b">{number.draw_time}</td>
          <td className="py-2 px-4 border-b">{number.numbers}</td>
          <td className="py-2 px-4 border-b">{number.created_at}</td>
        </tr>
        ))}
      </tbody>
      </table>
    </div>
  );
}

export default Lottery;