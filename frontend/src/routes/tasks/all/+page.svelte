<script lang="ts">
    import { goto } from '$app/navigation';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();
</script>

<div class="govuk-width-container">
	<div class="govuk-main-wrapper--auto-spacing" id="main-content" role="main">
		<div class="govuk-grid-row">
			<div class="govuk-grid-column-three-quarters">
				<h1 class="govuk-heading-xl">Task List</h1>
			</div>
			<div class="govuk-grid-column-one-quarter">
				<button
					class="govuk-button"
					type="button"
					onclick={() => goto('/tasks/new')}
				>
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
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>
