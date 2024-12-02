
import React, { useEffect, useState } from "react";
import { columns } from "../components/ui/tableSorted/columns";
import { DataTable } from "../components/ui/tableSorted/data-table"

export default function KenoLottery() {
  interface LotteryNumber {
    id: number;
    draw_date: string;
    game_name: string;
    numbers: string;
  }

  const [lotteryNumbers, setLotteryNumbers] = useState<LotteryNumber[]>([]);

  useEffect(() => {
    fetch("http://3.138.126.116:5001/lottery")
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setLotteryNumbers(data);
        } else {
          console.error("Fetched data is not an array:", data);
        }
      })
      .catch((error) => {
        console.error("Error fetching lottery numbers:", error);
      });
  }, []);

  return (
    <>
      <DataTable columns={columns} data={lotteryNumbers} />
    </>
  );
}