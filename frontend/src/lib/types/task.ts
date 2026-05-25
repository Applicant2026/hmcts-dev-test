export interface Task {
	id: number;
	title: string;
	description: string | null;
	status: string;
	status_display: string;
	due_date: string;
	due_date_display: string;
	created_at: string;
	updated_at: string;
}

export interface TaskPayload {
	title: string;
	description: string | null;
	status: string | null;
	due_date: string | null;
}

export interface TaskStatus {
	value: string;
	label: string;
}
