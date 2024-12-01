"use client";

import * as React from "react";
import { ColumnDef } from "@tanstack/react-table";
import { ArrowUpDown } from "lucide-react";
import { Button } from "../button";

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type LotteryNumber = {
	id: number;
	draw_date: string;
	game_name: string;
	numbers: string;
};

export const columns: ColumnDef<LotteryNumber>[] = [
	{
		accessorKey: "draw_date",
		header: ({ column }) => {
			return (
				<Button variant="ghost" onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}>
					Draw Date
					<ArrowUpDown className="ml-2 h-4 w-4" />
				</Button>
			);
		},
	},
	{
		accessorKey: "draw_time",
		header: "Draw Time",
	},
	{
		accessorKey: "game_name",
		header: "Game Name",
	},
	{
		accessorKey: "numbers",
		header: "Numbers",
	},
];
