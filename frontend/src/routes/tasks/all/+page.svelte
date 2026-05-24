<script lang="ts">
	import { goto } from '$app/navigation';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();

</script>

{#if data.tasks.count === 0}
	<div class="govuk-width-container">
		<div class="govuk-main-wrapper--auto-spacing" id="main-content" role="main">
			<h1 class="govuk-heading-xl">No tasks found</h1>
			<p class="govuk-body">There are currently no tasks. Click the button to create a new task.</p>
			<button class="govuk-button" type="button" onclick={() => goto('/tasks/new')}>
				Create New Task
			</button>
		</div>
	</div>
{:else}
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
						<th scope="col" class="govuk-table__header">Status</th>
						<th scope="col" class="govuk-table__header">Due At</th>
						<th scope="col" class="govuk-table__header">Actions</th>
					</tr>
				</thead>
				<tbody class="govuk-table__body">
					{#each data.tasks.results as task}
						<tr class="govuk-table__row">
							<th scope="row" class="govuk-table__header">{task.id}</th>
							<td class="govuk-table__cell cell--truncate">{task.title}</td>
							<td class="govuk-table__cell">{task.status_display}</td>
							<td class="govuk-table__cell">{task.due_date_display}</td>
							<td class="govuk-table__cell">
								<a class="govuk-link" href="/tasks/{task.id}">See more</a>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>
{/if}

<style>
	:global(.cell--truncate) {
		max-width: 200px;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}
</style>
