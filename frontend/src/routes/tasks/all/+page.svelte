<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import { TaskService } from '$lib/services/task-service';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();

	async function handleDelete(taskId: number) {
		if (confirm('Are you sure you want to delete this task?')) {
			try {
				await TaskService.deleteTask(taskId);
				// Invalidate the task list to refresh the data
				await invalidateAll();
			} catch (error) {
				console.error('Error deleting task:', error);
				alert('Failed to delete task. Please try again.');
			}
		}
	}
</script>

<div class="govuk-width-container">
	<div class="govuk-main-wrapper--auto-spacing" id="main-content" role="main">
		<div class="govuk-grid-row">
			<div class="govuk-grid-column-three-quarters">
				<h1 class="govuk-heading-xl">Task List</h1>
			</div>
			<div class="govuk-grid-column-one-quarter">
				<button class="govuk-button" type="button" onclick={() => goto('/tasks/new')}>
					Create New Task
				</button>
			</div>
		</div>

		<table class="govuk-table">
			<thead class="govuk-table__head">
				<tr class="govuk-table__row">
					<th scope="col" class="govuk-table__header">Task ID</th>
					<th scope="col" class="govuk-table__header">Title</th>
					<th scope="col" class="govuk-table__header">Description</th>
					<th scope="col" class="govuk-table__header">Status</th>
					<th scope="col" class="govuk-table__header">Due Date and Time</th>
					<th scope="col" class="govuk-table__header">Actions</th>
				</tr>
			</thead>
			<tbody class="govuk-table__body">
				{#each data.tasks.results as task}
					<tr class="govuk-table__row">
						<th scope="row" class="govuk-table__header">{task.id}</th>
						<td class="govuk-table__cell">{task.title}</td>
						<td class="govuk-table__cell">{task.description}</td>
						<td class="govuk-table__cell">{task.status_display}</td>
						<td class="govuk-table__cell">{task.due_date_display}</td>
						<td class="govuk-table__cell">
							<button class="govuk-button" type="button">Edit</button>
							<button
								type="submit"
								class="govuk-button govuk-button--warning"
								data-module="govuk-button"
								onclick={() => handleDelete(task.id)}
							>
								Delete
							</button>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>
