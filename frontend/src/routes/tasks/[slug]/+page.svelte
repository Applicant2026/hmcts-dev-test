<script lang="ts">
	import { goto } from '$app/navigation';
	import { TaskService } from '$lib/services/task-service';

	let { data } = $props();

	let createdAt = $derived(data.task.created_at);
	let updatedAt = $derived(data.task.updated_at);
	let formattedCreatedAt = $derived(createdAt ? new Date(createdAt).toLocaleString() : null);
	let formattedUpdatedAt = $derived(updatedAt ? new Date(updatedAt).toLocaleString() : null);

	async function handleDelete(taskId: number) {
		if (confirm('Are you sure you want to delete this task?')) {
			try {
				await TaskService.deleteTask(taskId);
				goto('/tasks/all');
			} catch (error) {
				console.error('Error deleting task:', error);
				alert('Failed to delete task. Please try again.');
			}
		}
	}
</script>

{#if data.task}
	<div class="govuk-width-container">
		<a href="/tasks/all/" class="govuk-back-link">Back</a>
		<h1 class="govuk-heading-l">Task Details</h1>
		<dl class="govuk-summary-list">
			<div class="govuk-summary-list__row">
				<dt class="govuk-summary-list__key">Title</dt>
				<dd class="govuk-summary-list__value">{data.task.title}</dd>
				<dd class="govuk-summary-list__actions">
					<a class="govuk-link" href="/tasks/{data.task.id}/edit"
						>Change<span class="govuk-visually-hidden"> title</span></a
					>
				</dd>
			</div>
			<div class="govuk-summary-list__row">
				<dt class="govuk-summary-list__key">Description</dt>
				<dd class="govuk-summary-list__value">{data.task.description}</dd>
				<dd class="govuk-summary-list__actions">
					<a class="govuk-link" href="/tasks/{data.task.id}/edit"
						>Change<span class="govuk-visually-hidden"> description</span></a
					>
				</dd>
			</div>
			<div class="govuk-summary-list__row">
				<dt class="govuk-summary-list__key">Status</dt>
				<dd class="govuk-summary-list__value">{data.task.status_display}</dd>
				<dd class="govuk-summary-list__actions">
					<a class="govuk-link" href="/tasks/{data.task.id}/edit"
						>Change<span class="govuk-visually-hidden"> status</span></a
					>
				</dd>
			</div>
			<div class="govuk-summary-list__row">
				<dt class="govuk-summary-list__key">Due</dt>
				<dd class="govuk-summary-list__value">{data.task.due_date_display}</dd>
				<dd class="govuk-summary-list__actions">
					<a class="govuk-link" href="/tasks/{data.task.id}/edit"
						>Change<span class="govuk-visually-hidden"> due date</span></a
					>
				</dd>
			</div>
		</dl>
		<div class="govuk-grid-row">
			<div class="govuk-grid-column-one-half">
				<h2 class="govuk-body">Created At: {formattedCreatedAt}</h2>
				<h2 class="govuk-body">Last Updated: {formattedUpdatedAt}</h2>
			</div>
		</div>
		<button
			type="submit"
			class="govuk-button govuk-button--warning"
			data-module="govuk-button"
			onclick={() => handleDelete(data.task.id)}
		>
			Delete Task
		</button>
	</div>
{:else}
	<div class="govuk-width-container">
		<div class="govuk-main-wrapper--auto-spacing" id="main-content" role="main">
			<h1 class="govuk-heading-xl">Task not found</h1>
			<p class="govuk-body">The task you are looking for does not exist.</p>
		</div>
	</div>
{/if}
