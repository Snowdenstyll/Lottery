// client/src/index.tsx
import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "./components/ui/table"; // Adjust the path as needed

function Index() {
	interface LotteryNumber {
		id: number;
		draw_date: string;
    created_at: string;
    game_name: string;
    numbers: string;
	}

	const [lotteryNumbers, setLotteryNumbers] = useState<LotteryNumber[]>([]);

	useEffect(() => {
		fetch("http://127.0.0.1:5001/lottery")
			.then((res) => res.json())
			.then((data) => {
        if (Array.isArray(data.lottery_numbers)) {
          console.log(data.lottery_numbers[0]);
					setLotteryNumbers(data.lottery_numbers);
				} else {
					console.error("Fetched data is not an array:", data);
				}
			})
			.catch((error) => {
				console.error("Error fetching lottery numbers:", error);
			});
	}, []);

	return (
    <div>
			<h1>Lottery Numbers</h1>
			<ul>
				{lotteryNumbers.map((number) => (
					<li key={number.id}>
						{number.draw_date}: {number.numbers}
					</li>
				))}
      </ul>
      <Table>
        <TableCaption>A list of your recent invoices.</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead className="w-[100px]">Invoice</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Method</TableHead>
            <TableHead className="text-right">Amount</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow>
            <TableCell className="font-medium">INV001</TableCell>
            <TableCell>Paid</TableCell>
            <TableCell>Credit Card</TableCell>
            <TableCell className="text-right">$250.00</TableCell>
          </TableRow>
        </TableBody>
      </Table>

		</div>
	);
}

const container = document.getElementById("root");
const root = createRoot(container!);
root.render(
	<BrowserRouter>
		<Routes>
			<Route path="/" element={<Index />} />
		</Routes>
	</BrowserRouter>
);

export default Index;
